function solution(clothes) {
    const clothesMap = {};
    
    for (const [name, type] of clothes) {
        if (clothesMap[type]) clothesMap[type]++;
        else clothesMap[type] = 1;
    }
    
    let ans = 1;
    for (const key in clothesMap) ans *= (clothesMap[key]+1);
    
    return ans-1;
}