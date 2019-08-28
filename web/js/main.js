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
    let pythonColor = eel.get_bg_color()();

    pythonColor.then(value => {
        document.body.style.backgroundColor = value;
    });

    setTimeout(setBgColor, 1000);
}

setTime();
setDate();
setBgColor();