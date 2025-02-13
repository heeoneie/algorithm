function solution(n) {
    n = String(n);
    let answer = [];
    for (let i=0; i<n.length; i++) answer.push(Number(n[i]));
    return Number(answer.sort((a,b) => b-a).join(""));
}