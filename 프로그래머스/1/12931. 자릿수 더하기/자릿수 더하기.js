function solution(n) {
    let answer = 0;
    n = String(n);
    for (let i=0; i<n.length; i++)
        answer += Number(n[i])
    return answer;
}