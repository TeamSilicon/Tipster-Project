//for scrolling to the current games
$(window).on("load", function(){
  var today = new Date();
  var dd = today.getDate();
  var hour = today.getHours().toString();
  var minute = today.getMinutes().toString();
  var find =  $('a.forecasts__item .forecasts__league .forecasts__date');
  var index = 0;
  find.text(function (i, game_time) {
    var hour2 = (game_time.split(':')[0]).replace(/^\s+|\s+$/g, "");
    var minute2 = (game_time.split(':')[1]).replace(/^\s+|\s+$/g, "");

    var date1 = new Date(today.getYear(), today.getMonth(),dd, hour, minute);
    var game_date = new Date(today.getYear(), today.getMonth(), dd,hour2, minute2);

    distance =  game_date - date1;
    var days = Math.floor(distance / (1000 * 60 * 60 * 24));

    var hours = Math.floor((distance % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));

    var minutes= Math.floor((distance % (1000 * 60 * 60)) / (1000 * 60));

    // var seconds= Math.floor((distance % (1000 * 60 )) / (1000));
    if (days<0) {
      days = days+1;
    }
    if (hours<0) {
      hours = hours+1;
    }
    var distance_in_minutes= (hours * 60) + minutes;
    match_status = "";
    index ++;
    if (distance_in_minutes < -115) {
      match_status = "finished";
      $("div.forecasts__list > .forecasts__item:nth-child("+index+") > i.flag > img").attr("src", "/static/css/assets/fin.png");
    }
    else if(distance_in_minutes>=-115 && distance_in_minutes < 0){
      match_status = "ongoing";
      $("div.forecasts__list > .forecasts__item:nth-child("+index+") > i.flag > img").attr("src", "/static/css/assets/z-live.gif");

    }
    else if (distance_in_minutes >=0 && distance_in_minutes < 90 ) {
      match_status = "abtto_start";
      $("div.forecasts__list > .forecasts__item:nth-child("+index+") > i.flag > img").attr("src", "/static/css/assets/about.png");
      document.querySelector("div.forecasts__list > a:nth-child("+index+")").className += ' abtto_start';
    }
    else {
      match_status = "later";
      $("div.forecasts__list > .forecasts__item:nth-child("+index+") > i.flag > img").attr("src", "/static/css/assets/l8.png");
    }
    // console.log(match_status);
    // console.log(days + "\n" + hours + "\n" + minutes +"\n" );

  });
  var numItems = $('.abtto_start').length;
  if(numItems >= 1){
    var target = $("div.forecasts__list").find( ".abtto_start").first();
      $('html, body').stop().animate({
        scrollTop: target.offset().top
      }, 2000);
    }
});
