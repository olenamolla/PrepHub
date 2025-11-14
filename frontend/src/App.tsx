import { useEffect, useState } from 'react'
import reactLogo from './assets/react.svg'
import viteLogo from '/vite.svg'
import './App.css'
import api from './services/api'


// TS interface to help catch errors early
interface Problem {
  id: number;
  title: string;
  difficulty: string;
  topic: string;
  notes: string;
  solved_date: string;
}
function App() {
  const [problems, setProblems] = useState<Problem[]>([])
  const [loading, setLoading] = useState(true)
  const [error, setError] = useState<string | null>(null)

  const [count, setCount] = useState(0)


  useEffect( () => {
    const fetchProblems = async () => {
      try {
        setLoading(true)
        const response = await api.get('/problems/')
        setProblems(response.data)
        setError(null)
      } catch (err) {
        setError('Failed to load problems. Make sure Django server is running.')
        console.error('Error fetching problems:', err)
      } finally {
        setLoading(false)
      }
    }
    fetchProblems()
  },
 [])

  return (
    <>
      <div>
        <a href="https://vite.dev" target="_blank">
          <img src={viteLogo} className="logo" alt="Vite logo" />
        </a>
        <a href="https://react.dev" target="_blank">
          <img src={reactLogo} className="logo react" alt="React logo" />
        </a>
      </div>
      <h1>Vite + React</h1>
      <div className="card">
        <button onClick={() => setCount((count) => count + 1)}>
          count is {count}
        </button>
        <p>
          Edit <code>src/App.tsx</code> and save to test HMR
        </p>
      </div>
      <p className="read-the-docs">
        Click on the Vite and React logos to learn more
      </p>
    </>
  )
}

export default App
