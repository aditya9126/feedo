var con=0, nat=0, out=0;

function confidence(x){
	con = x;
	var ele = document.getElementsByClassName("star_c");
	
	for(i=0;i<x;i++){
		var s = "starc"+(i+1);
		document.getElementById(s).src = "static/profile_icon.svg";
	}
	for(i=x;i<ele.length;i++){
		var s = "starc"+(i+1);
		document.getElementById(s).src = "static/star_icon.svg";
	}
	
	switch(x){
		case 1:
			document.getElementById("confidence_smiley").src = "static/smiley1.svg";
			break;
		case 2:
			document.getElementById("confidence_smiley").src = "static/smiley2.svg";
			break;
		case 3:
			document.getElementById("confidence_smiley").src = "static/smiley3.svg";
			break;
		case 4:
			document.getElementById("confidence_smiley").src = "static/smiley4.svg";
			break;
		case 5:
			document.getElementById("confidence_smiley").src = "static/smiley5.svg";
			
	}
	
}

function outspoken(x){
	out=x;
	var ele = document.getElementsByClassName("star-o");
	for(i=0;i<x;i++){
		var s = "staro"+(i+1);
		document.getElementById(s).src = "static/profile_icon.svg";
	}
	for(i=x;i<ele.length;i++){
		var s = "staro"+(i+1);
		document.getElementById(s).src = "static/star_icon.svg";
	}
	switch(x){
		case 1:
			document.getElementById("outspoken_smiley").src = "static/smiley1.svg";
			break;
		case 2:
			document.getElementById("outspoken_smiley").src = "static/smiley2.svg";
			break;
		case 3:
			document.getElementById("outspoken_smiley").src = "static/smiley3.svg";
			break;
		case 4:
			document.getElementById("outspoken_smiley").src = "static/smiley4.svg";
			break;
		case 5:
			document.getElementById("outspoken_smiley").src = "static/smiley5.svg";
	}
	var outspoken={"value": x};
	out= JSON.stringify(outspoken);
}

function nature(x){
	nat=x;
	var ele = document.getElementsByClassName("star_n");
	for(i=0;i<x;i++){
		var s = "starn"+(i+1);
		document.getElementById(s).src = "static/profile_icon.svg";
	}
	for(i=x;i<ele.length;i++){
		var s = "starn"+(i+1);
		document.getElementById(s).src = "static/star_icon.svg";
	}
	switch(x){
		case 1:
			document.getElementById("nature_smiley").src = "static/smiley1.svg";
			break;
		case 2:
			document.getElementById("nature_smiley").src = "static/smiley2.svg";
			break;
		case 3:
			document.getElementById("nature_smiley").src = "static/smiley3.svg";
			break;
		case 4:
			document.getElementById("nature_smiley").src = "static/smiley4.svg";
			break;
		case 5:
			document.getElementById("nature_smiley").src = "static/smiley5.svg";
	}
	
}

function myFun(){
	document.getElementById("demo").innerHTML = "I'm in javascript";
	//var data = {nature:nat,confidence:con,ouspoken:out};
	var data = {amit:'profile'};
	$.ajax({
		type: 'POST',
		url: '/<name>',
		data: JSON.stringify(data),
		dataType: 'json',
		contentType: 'application/json; charset=utf-8'
	}).done(function(msg) {
		alert("Data Saved: " + msg);
	});
}

