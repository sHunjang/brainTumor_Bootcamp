// src/pages/ResultPage.jsx
import React from 'react';
import { useLocation, useNavigate } from 'react-router-dom';

import Navbar from '../components/Navbar';
import CTImageBox from '../components/CTImageBox';
import ResultTable from '../components/ResultTable';
import DiagnosisNote from '../components/DiagnosisNote';
import AnalyzeAgainButton from '../components/AnalyzeAgainButton';

const ResultPage = () => {
  const location = useLocation();
  const navigate = useNavigate();
  const result = location.state;

  if (!result) {
    navigate('/');
    return null;
  }

  const bbox = {
    top: result.bbox_top,
    left: result.bbox_left,
    width: result.bbox_width,
    height: result.bbox_height,
  };

  return (
    <div>
      <Navbar />
      <div style={{ padding: '0' }}>
        {/* 제목과 진단요약 */}
        <div style={{ width: '60%', margin: '40px auto 0 auto', textAlign: 'left' }}>
          <h2 style={{ marginBottom: '8px' }}>CT 소견서 결과</h2>
          <h4 style={{ marginTop: 0 }}>{result.location}: {result.diagnosis}</h4>
        </div>

        {/* 이미지 중앙 정렬 */}
        <div style={{ textAlign: 'center', marginTop: '20px' }}>
          <CTImageBox imageUrl={result.image_url} box={bbox} />
        </div>

        {/* 결과표 */}
        <ResultTable
          location={result.location}
          coords={result.coords}
          size={result.size}
          confidence={result.confidence}
          coord_x1={result.coord_x1}
          coord_y1={result.coord_y1}
          coord_x2={result.coord_x2}
          coord_y2={result.coord_y2}
          description={result.description}
          symptom={result.symptom}
        />

        {/* 소견서 */}
        <DiagnosisNote text={result.comment} />

        {/* 다시 분석 버튼 */}
        <div style={{ textAlign: 'center', marginTop: '40px', marginBottom: '40px' }}>
          <AnalyzeAgainButton />
        </div>
      </div>
    </div>
  );
};

export default ResultPage;
