import React, { useState, useEffect } from 'react';

const App = () => {
  const [likes, setLikes] = useState(0);

  const handleLikeClick = async () => {
    // Increment local like counter
    setLikes(likes + 1);

    // Send request to the backend to process the like
    await fetch('http://localhost:8000/api/likes', {
      method: 'POST',
      // Additional headers and body can be added here
    });
  };

  useEffect(() => {
    const fetchLikes = async () => {
      // Fetch likes from the backend every 5 seconds
      const response = await fetch('http://localhost:8000/api/likes');
      const data = await response.json();
      setLikes(data.likes);
    };

    const intervalId = setInterval(fetchLikes, 5000);

    return () => clearInterval(intervalId);
  }, []);

  return (
    <div>
      <p>Likes: {likes}</p>
      <button onClick={handleLikeClick}>Like</button>
    </div>
  );
};

export default App;
