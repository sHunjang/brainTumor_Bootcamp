import React, { useRef, useState } from 'react';

const UploadBox = ({ onFileSelect }) => {
  const fileInputRef = useRef();
  const [previewUrl, setPreviewUrl] = useState(null);

  const handleClick = () => {
    fileInputRef.current.click();
  };

  const handleFileChange = (e) => {
    const file = e.target.files[0];
    if (file) {
      // 미리보기 URL 생성
      const reader = new FileReader();
      reader.onloadend = () => {
        setPreviewUrl(reader.result);
      };
      reader.readAsDataURL(file);

      onFileSelect(file);
    }
  };

  return (
    <div style={styles.container}>
      <div style={styles.box}>
        <p><strong>사진 업로드</strong></p>
        <p style={{ fontSize: '12px' }}>Drag and drop or click to upload</p>
        <button onClick={handleClick} style={styles.button}>Upload Photo</button>
        <input
          type="file"
          accept="image/*"
          onChange={handleFileChange}
          ref={fileInputRef}
          style={{ display: 'none' }}
        />
        {/* 미리보기 이미지 렌더링 */}
        {previewUrl && (
          <div style={{ marginTop: '20px' }}>
            <img
              src={previewUrl}
              alt="미리보기"
              style={{ maxWidth: '400px', maxHeight: '300px', border: '1px solid #eee', borderRadius: '6px' }}
            />
          </div>
        )}
      </div>
    </div>
  );
};

const styles = {
  container: {
    textAlign: 'center',
    marginTop: '50px'
  },
  box: {
    border: '2px dashed #ccc',
    borderRadius: '8px',
    padding: '40px',
    width: '1200px',
    margin: '0 auto'
  },
  button: {
    marginTop: '12px',
    padding: '10px 16px',
    backgroundColor: '#f6f6f6',
    border: '1px solid #ccc',
    borderRadius: '6px',
    cursor: 'pointer'
  }
};

export default UploadBox;
