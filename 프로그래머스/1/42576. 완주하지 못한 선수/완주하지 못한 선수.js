function solution(participant, completion) {
    const participantMap = {};
    
    for (const p of participant) {
        if (participantMap[p]) participantMap[p]++;
        else participantMap[p] = 1;
    }
    
    for (const c of completion) {
        participantMap[c]--;
        if (participantMap[c] === 0) delete participantMap[c];
    }
    
    return Object.keys(participantMap)[0];
}