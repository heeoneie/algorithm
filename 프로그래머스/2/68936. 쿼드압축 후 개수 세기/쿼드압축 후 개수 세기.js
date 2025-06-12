function solution(arr) {
    let answer = [0, 0];
    function compress(x, y, size) {
        let first = arr[x][y];
        let allSame = true;
        for(let i=x; i<x+size; i++) {
            for(let j=y; j<y+size; j++) {
                if(arr[i][j] !== first) {
                    allSame = false;
                    break;
                }
            }
            if(!allSame) break;
        }
        if(allSame) {
            answer[first]++;
        } else {
            let newSize = size / 2;
            compress(x, y, newSize);
            compress(x, y+newSize, newSize);
            compress(x+newSize, y, newSize);
            compress(x+newSize, y+newSize, newSize);
        }
    }
    compress(0, 0, arr.length);
    return answer;
}