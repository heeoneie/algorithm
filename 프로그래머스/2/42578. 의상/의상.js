function solution(clothes) {
    const clothesMap = {};
    for (const [name, type] of clothes) {
        if (!clothesMap[type]) clothesMap[type] = 1;
        else clothesMap[type]++;
    }
    let ans = 1;
    for (const key in clothesMap) ans *= (clothesMap[key]+1);
    
    return ans-1; 
}