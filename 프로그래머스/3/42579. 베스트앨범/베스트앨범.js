function solution(genres, plays) {
    const albumMap = {};
    
    for (let i=0; i<genres.length; i++) {
        if (!albumMap[genres[i]]) albumMap[genres[i]] = { totalPlay: 0, songs: [] };
        albumMap[genres[i]].totalPlay += plays[i];
        albumMap[genres[i]].songs.push({ id: i, play: plays[i]} );
    }
    
    const sortedGenres = Object.values(albumMap).sort((a,b) => b.totalPlay - a.totalPlay );
    const ans = [];
    
    for (const genre of sortedGenres) {
        genre.songs.sort((a,b) => b.play - a.play || a.id - b.id);
        ans.push(genre.songs[0].id);
        if (genre.songs.length > 1) ans.push(genre.songs[1].id);
    }
    
    return ans;
}