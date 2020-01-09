from flask import render_template, url_for, flash, redirect, request
from feedo import app, db, bcrypt
from feedo.forms import JoinForm, SigninForm, SearchForm, RateForm, FeedbackForm
from feedo.models import User, Feedback, Rate
from flask_login import login_user, current_user, logout_user, login_required
#________________________________________________________________________________________________________________________________________________________________
home_feedo = './static/home_feedo.svg'
thefeedo_1 = './static/thefeedo_1.png'
feedo_logo = './static/feedo_logo.svg'
profile_icon = './static/profile_icon.svg'
profile_pic = './static/profile_pic.jpg'
star_icon = './static/star_icon.svg'
smiley1 = './static/smiley1.svg'
gif_icon = './static/gif_icon.svg'
badge_icon = './static/badge_icon.svg'
#________________________________________________________________________________________________________________________________________________________________
@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', home_feedo=home_feedo, thefeedo_1 = thefeedo_1)
#________________________________________________________________________________________________________________________________________________________________
@app.route("/signin", methods=['GET','POST'])
def signin():
    if current_user.is_authenticated:
        return redirect(url_for('profile', name= current_user.username))
   
    form = SigninForm()
    user = User.query.filter_by(username=str(form.username.data)).first()
    if user and bcrypt.check_password_hash(user.password, form.password.data):
        login_user(user, remember= form.remember.data) #error: remember is taking true all the time.
        next_page = request.args.get('next')           #tip: to redirect us to the page which we wanted to see but needed login. check the url when you do testing and you will get it..
        
        return redirect(next_page) if next_page else redirect(url_for('profile', name= current_user.username))
    else:
        flash('Login Unsuccessful. Please check username and password', 'danger')

    return render_template('signin.html', thefeedo_1 = thefeedo_1, form=form)
#________________________________________________________________________________________________________________________________________________________________
@app.route("/join", methods=['GET','POST'])
def join():
    if current_user.is_authenticated:
        return redirect(url_for('profile', name= current_user.username))
    
    form = JoinForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(username=form.username.data,
                    name=form.name.data,
                    email=form.email.data,
                    password=hashed_password)

        db.session.add(user)
        db.session.commit()
        
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('signin'))
    
    return render_template('join.html', thefeedo_1 = thefeedo_1, form=form)
#________________________________________________________________________________________________________________________________________________________________
@app.route("/<name>", methods=['GET','POST'])
@login_required
def profile(name):
    rd=[]
    if name == current_user.username:   #tip: then compair it to all the database that you have and return the output
        form = SearchForm()

        if form.validate_on_submit():
            searched_user = User.query.filter_by(username=str(form.username.data)).first()  #tip: at this point searched_user can be empty... so we have to check feature more

            if current_user == searched_user: return redirect(url_for('profile', name= current_user.username))
            elif current_user != searched_user and searched_user: return redirect(url_for('profile', name= searched_user.username))

        feed_msg = Feedback.query.filter_by(recevier_username= name) # ToDo: order by time bhi karna h


        confidence,nature,outspoken,avg=0,0,0,0
        con_count, nat_count, out_count, avg_count= 0,0,0,0
        for star in Rate.query.filter_by(recevier_username= name):
            if star.confidence != None:
                confidence= confidence+star.confidence
                con_count= con_count+1

            if star.nature != None:
                nature= nature+star.nature
                nat_count = nat_count+1

            if star.outspoken != None:
                outspoken= outspoken+star.outspoken
                out_count = out_count+1

            if star.avg != None:
                avg= avg+star.avg
                avg_count = avg_count+1
        if con_count==0 or nat_count==0 or out_count==0 or avg_count==0:
            pass
        else:
            confidence= confidence//con_count
            nature= nature//nat_count
            outspoken= outspoken//out_count
            avg= avg//avg_count
        #will not give decimal values. bocz we cannot loop on decimal, which we are doing in HTML

        c_user = User.query.filter_by(username=str(name)).first()


        return render_template('profile.html',
                               feedo_logo=feedo_logo,     profile_icon = profile_icon,
                               profile_pic=profile_pic,   star_icon=star_icon,
                               form=form,                 name=c_user.name,
                               username= c_user.username,
                               bio= c_user.bio, feed_msg=feed_msg, 
                               confidence= confidence, nature=nature, outspoken=outspoken)
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------
    elif name != current_user.username:
        
        form = SearchForm()
        r_form= RateForm()
        feed_form= FeedbackForm()

#-----------------------------------------------
        if form.validate_on_submit():
            searched_user = User.query.filter_by(username=str(form.username.data)).first() 

            if current_user == searched_user: return redirect(url_for('profile', name= current_user.username))
            elif current_user != searched_user and searched_user: return redirect(url_for('profile', name= searched_user.username))
        else:
            pass


        if request.get_json() != None:
            rd.append(request.get_json())
            print("profile" , rd)
            total=0
            count=0

            if rd[0]['confidence'] != None:
                count= count+1
                total= total+ rd[0]['confidence']
            if rd[0]['nature'] != None:
                count= count+1
                total= total+ rd[0]['nature']
            if rd[0]['outspoken'] != None:
                count= count+1
                total= total+ rd[0]['outspoken']
            if count!=0:
                rate = Rate(sender_username=current_user.username, recevier_username="aman joshi", #name nahi aarha h!
                        confidence= rd[0]['confidence'],
                        nature= rd[0]['nature'],
                        outspoken= rd[0]['outspoken'],
                        avg= total/count) 
                db.session.add(rate)
                db.session.commit()
        else:
            pass
        
        if feed_form.validate_on_submit() and feed_form.feedback.data != '':
            feedback = Feedback(sender_username= current_user.username, recevier_username=name, message= feed_form.feedback.data)
            db.session.add(feedback)
            db.session.commit()
        else:
            pass
       
#-------------------------------------------------------------------
        
        s_user= User.query.filter_by(username=str(name)).first()
        return render_template('profile.html',
                               feedo_logo=feedo_logo,   profile_icon = profile_icon,
                               profile_pic=profile_pic, star_icon=star_icon,
                               smiley1=smiley1,         gif_icon=gif_icon,
                               badge_icon=badge_icon,   form=form,
                               name=s_user.name,        username=s_user.username, bio=s_user.bio,
                               r_form=r_form,
                               feed_form=feed_form)
    else:
        print("handled i think")
#________________________________________________________________________________________________________________________________________________________________
@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for('home'))
#________________________________________________________________________________________________________________________________________________________________
