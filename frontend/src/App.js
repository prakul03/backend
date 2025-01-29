import { Routes, Route } from 'react-router-dom';
import SignUpPage from './pages/SignUpPage';
import LandingPage from './pages/LandingPage';

function App(){
  return (
    <Routes>
      <Route path="/" element={<LandingPage/>} />
      <Route path="/signup" element={<SignUpPage />} />
    </Routes>
  );
}
export default App;