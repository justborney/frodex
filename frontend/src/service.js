export const get_posts = async () => {
    return await fetch('http://localhost:8080/api/getPosts')
}

export const post_like = async (uuid) => {
    return await fetch(`http://localhost:8080/api/like/${uuid}`, {
        method: 'POST',
    })
}