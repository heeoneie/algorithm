/*
조합으로 만든 후 각 요소를 더 했을 때 0이면 answer 증가
nC3
*/
function getCombinations(arr, selectNumber) {
    const results = [];
    if (selectNumber === 1) return arr.map((value) => [value]);

    arr.forEach((fixed, index, origin) => {
        const rest = origin.slice(index + 1);
        const combinations = getCombinations(rest, selectNumber - 1);
        const attached = combinations.map((combination) => [fixed, ...combination]);
        results.push(...attached);
    });
    return results;
}

function solution(number) {
    let answer = 0;
    const combinations = getCombinations(number, 3);
    for (let i = 0; i<combinations.length; i++) {
        let sum = 0;
        for (let j = 0; j<3; j++) {
            sum = sum + combinations[i][j];
        }
        if (sum == 0) {
            answer++;
        }
    }
    return answer;
}