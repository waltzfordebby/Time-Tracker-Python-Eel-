const timeContainer = document.getElementById('time');
const dateContainer = document.getElementById('date');


function setTime() {
    let pythonTime = eel.get_time()();

    pythonTime.then(value => {
        timeContainer.innerHTML = value;
    });

    setTimeout(setTime, 1000);
}

function setDate() {
    let pythonDate = eel.get_date()();

    pythonDate.then(value => {
        dateContainer.innerHTML = value;
    });

    setTimeout(setDate, 1000);
}

function setBgColor() {
    let pythonBGColor = eel.get_bg_color()();

    pythonBGColor.then(value => {
        document.body.style.backgroundColor = value;
    });

    setTimeout(setBgColor, 1000);
}

function setFontColor() {
    let pythonFontColor = eel.get_font_color()();

    pythonFontColor.then(value => {
        document.body.style.color = value;
    });
}

setTime();
setDate();
setBgColor();
setFontColor();