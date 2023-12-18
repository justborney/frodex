import React, { useState, useEffect } from 'react';
import {get_posts, post_like} from './service';

const App = () => {
  const [posts, setPosts] = useState([]);

  useEffect(() => {
    const fetchPosts = async () => {
      try {
        const postsData = await get_posts();

        setPosts(postsData);
      } catch (error) {
        console.error('Error fetching posts:', error);
      }
    };

    setInterval(() => fetchPosts(), 5000);
  }, []);

  const likePost = async (postId) => {
    try {
      await post_like(postId);
      setPosts(posts.map((item) => ({
        ...item,
        likes: item.post === postId ? (item.likes + 1) : item.likes
      })))
    } catch (err) {
      console.error(err)
    }
  };

  return (
    <div>
      {posts && posts.sort((a, b)=> a.post < b.post).map((item) => (
        <div key={item.post} style={{margin: "10px"}}>
          <p>{item.post}</p>
          <button onClick={() => likePost(item.post)}>Лайкнуть</button>
          <p>Count: {item.likes}</p>
        </div>
      ))}
    </div>
  );
};

export default App;
