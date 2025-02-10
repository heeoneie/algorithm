function solution(arr) {
    return arr.reduce((current, next) => current + next) / arr.length;
}