function solution(t, p) {
    let answer = 0;
    const pLen = p.length;
    const pNum = Number(p);
    
    for (let i = 0; i<=t.length - pLen; i++) {
        const subStr = t.slice(i, pLen+i);
        if (subStr <= pNum) {
            answer++;
        }
    }
    return answer;
}