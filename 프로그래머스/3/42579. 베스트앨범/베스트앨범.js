function solution(genres, plays) {
    const albumMap = {};
    for (let i=0; i<genres.length; i++) {
        if (!albumMap[genres[i]]) albumMap[genres[i]] = { totalPlays: 0, songs: [] };
        albumMap[genres[i]].totalPlays += plays[i];
        albumMap[genres[i]].songs.push({ id: i, plays: plays[i] });
    }
    
    const sortedGenres = Object.values(albumMap).sort((a,b) => b.totalPlays - a.totalPlays);
    const ans = [];
    for (const genre of sortedGenres) {
        genre.songs.sort((a,b) => b.plays - a.plays || a.id - b.id);
        ans.push(genre.songs[0].id);
        if (genre.songs.length > 1) ans.push(genre.songs[1].id);
    }
    return ans;
}