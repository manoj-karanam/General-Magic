import './App.css';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import Login from './Components/Login';
import Footer from './Components/Footer';
import SignUp from './Components/SignUp';

function App() {
  return (
    <Router>
      <div className="App">
        <Routes>
        <Route path="/" element={<Login/>} /> 
        <Route path="/signup" element={<SignUp/>} />
        </Routes>
        <Footer />
      </div>
    </Router>
  );
}


export default App;
