// 각 앱에 맞는 커스텀 js

if (!Custom) {
    var Custom = {};
}

if(!Navi) {
    var Navi = {};
}

if (!Weather) {
    var Weather = {};
}

Weather.getIconClass = function () {
    var desc = Weather.data.weather[0].description;
    if (desc === undefined) return '';
    if (desc == '맑음') return 'wi-day-sunny'
}

if (navigator.geolocation) {
    navigator.geolocation.getCurrentPosition(function (position) {
        Navi.lat = position.coords.latitude;
        Navi.lon = position.coords.longitude;
    }, function (error) {
        console.error(error);
        // 에러인 경우 강남을 기본으로 하도록
        // 37.498058466300755, 127.02774299278178
        Navi.lat = 37.498058466300755
        Navi.lon = 127.02774299278178
    }, {
        enableHighAccuracy: false,
        maximumAge: 0,
        timeout: Infinity
    });
}