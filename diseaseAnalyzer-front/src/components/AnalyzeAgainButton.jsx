//다른이미지 분석 버튼
import React from 'react';

const AnalyzeAgainButton = () => {
  return (
    <button style={styles.button} onClick={() => window.location.href = '/'}>
      다른 이미지 분석
    </button>
  );
};

const styles = {
  button: {
    marginTop: '30px',
    marginbottom : "30px",
    padding: '10px 18px',
    backgroundColor: '#111',
    color: '#fff',
    border: 'none',
    borderRadius: '6px',
    cursor: 'pointer'
  }
};

export default AnalyzeAgainButton;
