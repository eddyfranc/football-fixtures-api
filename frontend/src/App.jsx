import { BrowserRouter, Routes, Route } from "react-router-dom";
import Navbar from "./Components/Navbar";
import HomePage from "./Components/HomePage";
import NotFound from "./Components/NotFound";
import "./index.css";


function App() {
  return (
    <>
      <BrowserRouter>
        <Navbar />
        <Routes>
          <Route path="/" element={<HomePage />} />
          <Route path='/notfound' element={<NotFound/>} />
        </Routes>
      </BrowserRouter>
    </>
  );
}

export default App;
