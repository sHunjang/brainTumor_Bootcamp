// src/components/DiagnosisNote.jsx
import React from 'react';

const DiagnosisNote = ({ text }) => {
  return (
    <div style={styles.note}>
      <h4 style={styles.title}>임상 소견</h4>
      <p style={styles.body}>{text}</p>
    </div>
  );
};

const styles = {
  note: {
    width: '60%',
    margin: '0 auto 40px auto',
    textAlign: 'left',
  },
  title: {
    fontSize: '18px',
    marginBottom: '12px',
  },
  body: {
    fontSize: '14px',
    lineHeight: '1.7',
    color: '#333',
    whiteSpace: 'pre-line'
  }
};

export default DiagnosisNote;
