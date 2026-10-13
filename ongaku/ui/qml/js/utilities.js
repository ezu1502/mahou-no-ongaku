

function clamp(variable, minimum, maximum){
    return Math.max(minimum, Math.min(maximum, variable));
}

function format_time(seconds){
    let minutes = Math.floor(seconds / 60);
    let secs = Math.floor(seconds % 60);

    return minutes + ":" + String(secs).padStart(2, "0");
}
