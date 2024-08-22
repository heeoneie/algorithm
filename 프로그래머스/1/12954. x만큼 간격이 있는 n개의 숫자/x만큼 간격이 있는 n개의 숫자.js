function solution(x, n) {
    let answer = [];
    for(let i=x; answer.length<n; x+=i) answer.push(x);
    return answer;
}