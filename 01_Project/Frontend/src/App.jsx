import { useState } from 'react';
import './App.css'

function App() {
  const [userquery, setUserquery] = useState('');
  const [gptoutput, setGptoutput] = useState('');
  const [loading, setLoading] = useState(false);

  const sendQuery = async (e) => {
    e.preventDefault();
    setLoading(true);

    const res = await fetch('http://localhost:3000', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ query: userquery })
    });

    const data = await res.json();
    setGptoutput(data.answer);

    setLoading(false);
  };

  return (
    <div>
      <div className="res-box">
        <p>{loading ? "Loading..." : gptoutput}</p>
      </div>
      <form onSubmit={sendQuery}>
        <input  type="text" value={userquery} onChange={(e) => setUserquery(e.target.value)} className='userinp' />
        <button type="submit">Send</button>
      </form>
    </div>
  );
}

export default App;
