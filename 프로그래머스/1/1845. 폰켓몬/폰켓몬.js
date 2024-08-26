function solution(nums) {
    const poketmons = new Set(nums);
    return Math.min(poketmons.size, nums.length/2);
}