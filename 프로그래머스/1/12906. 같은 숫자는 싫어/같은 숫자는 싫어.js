function solution(arr) {
    const stack = [arr[0]];
    
    for (let i=1; i<arr.length; i++) {
        if (arr[i] != stack[stack.length-1]) stack.push(arr[i]);
    }
    return stack;
}