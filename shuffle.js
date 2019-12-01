$(".gallery").html($(".gallery .photo-figure").sort(function(){
	return Math.random()-0.5;
}));