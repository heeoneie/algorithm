function solution(nums) {
    const poketmonMap = new Set(nums);
    return Math.min(poketmonMap.size, nums.length/2);
}