// src/pages/MainPage.jsx
import React, { useState } from 'react';
import Navbar from '../components/Navbar';
import UploadBox from '../components/UploadBox';
import { useNavigate } from 'react-router-dom';

const MainPage = () => {
  const navigate = useNavigate();
  const [imageFile, setImageFile] = useState(null);
  const [loading, setLoading] = useState(false);

  const handleFileChange = (file) => {
    setImageFile(file);
  };

  const handleCheckReport = async () => {
    if (!imageFile) {
      alert("이미지를 업로드해주세요.");
      return;
    }

    setLoading(true);

    try {
      // 1. FormData에 파일 추가
      const formData = new FormData();
      formData.append('file', imageFile);

      // 2. 백엔드에 POST 요청 (엔드포인트/포트는 환경에 맞게 수정)
      const response = await fetch('http://localhost:8000/api/upload-image/', {
        method: 'POST',
        body: formData,
      });

      if (!response.ok) {
        throw new Error('서버 오류가 발생');
      }

      // 3. 결과 JSON 파싱
      const data = await response.json();

      // 4. 결과 페이지로 이동 (state로 결과 전달)
      navigate('/result', { state: data });

    } catch (error) {
      alert(error.message || '예측 중 오류가 발생');
    } finally {
      setLoading(false);
    }
  };

  return (
    <div>
      <Navbar />
      <UploadBox onFileSelect={handleFileChange} />
      <div style={{ textAlign: 'center', marginTop: '20px' }}>
        <button
          onClick={handleCheckReport}
          style={styles.button}
          disabled={loading}
        >
          {loading ? '분석 중...' : '소견서 확인'}
        </button>
      </div>
    </div>
  );
};

const styles = {
  button: {
    padding: '10px 20px',
    border: 'none',
    backgroundColor: '#eee',
    cursor: 'pointer',
    borderRadius: '6px',
    fontSize: '25px'
  }
};

export default MainPage;
