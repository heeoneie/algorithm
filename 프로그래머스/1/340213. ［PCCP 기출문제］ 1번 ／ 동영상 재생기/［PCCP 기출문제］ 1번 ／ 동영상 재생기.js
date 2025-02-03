function changeSec(time) {
    let [min, sec] = time.split(':').map(Number);
    return 60 * min + sec;
}
function solution(video_len, pos, op_start, op_end, commands) {
    let pos_sec = changeSec(pos);
    let op_start_sec = changeSec(op_start);
    let op_end_sec = changeSec(op_end);
    let video_sec = changeSec(video_len);
    
    if (op_start_sec <= pos_sec && pos_sec <= op_end_sec)
        pos_sec = op_end_sec;
    
    for (let command of commands) {
        if (command == "prev")
            pos_sec -= 10;
        else
            pos_sec += 10;
        if (pos_sec > video_sec)
            pos_sec = video_sec;
        else if (pos_sec < 0)
            pos_sec = 0;
        if (op_start_sec <= pos_sec && pos_sec <= op_end_sec)
            pos_sec = op_end_sec;
    }
    
    let min = String(Math.floor(pos_sec / 60)).padStart(2, '0');
    let sec = String(pos_sec % 60).padStart(2, '0');
    
    return `${min}:${sec}`;
}