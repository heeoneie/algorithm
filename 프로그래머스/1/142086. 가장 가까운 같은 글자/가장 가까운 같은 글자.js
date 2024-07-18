function solution(s) {
    let answer = [-1];
    for (let i = 1; i<s.length; i++) {
        const prevIdx = s.lastIndexOf(s[i], i-1);
        if (prevIdx == -1) answer.push(-1);
        else answer.push(i - prevIdx);
    }
    return answer;
}