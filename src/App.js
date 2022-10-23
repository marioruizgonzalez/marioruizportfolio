import Sidebar from './components/Sidebar';
import Resume from './components/Resume';
import Home from './components/Home';
import { BrowserRouter, Route, Routes } from 'react-router-dom';


function App() {
  return (
    <div className="main">
      <Sidebar />


      <div >
      <h1>Marine Mammals</h1>
      <BrowserRouter>
      <Routes>
      <Route exact path="/" element={<Home />} />
      <Route exact path="/resume" element={<Resume />} />
      
    </Routes>
      </BrowserRouter>
    </div>

    </div>
  )
}

export default App