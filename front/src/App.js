import React from 'react';
import Sidebar from './components/Sidebar';
import HeroSection from './components/Herosection';
import './app.css'; // CSS 파일을 이용하여 스타일을 적용
function App() {
  return (
    <div className="app">
      <Sidebar />
      <HeroSection />
      {/* 기타 컴포넌트 또는 콘텐츠 */}
    </div>
  );
}

export default App;