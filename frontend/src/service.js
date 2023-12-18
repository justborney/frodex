export const get_posts = async () => {
    const response = await fetch('http://localhost:8001/api/likes');
    return response.json();
}

export const post_like = async (uuid) => {
    return await fetch('http://localhost:8001/api/likes', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({
        post: uuid,
      }),
    })
}