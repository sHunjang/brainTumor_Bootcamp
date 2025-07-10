// ct 이미지 보여주는 컴포넌트
import React, { useState } from 'react';
// import defaultImage from '../assets/image/default_ct.jpg';

const BACKEND_URL = 'http://localhost:8000';


const CTImageBox = ({ imageUrl }) => {

  const [imgError, setImgError] = useState(false);

  // 백엔드에서 받은 imageUrl이 있을 때만 서버 주소를 붙여서 사용
  const fullImageUrl = imageUrl ? `${BACKEND_URL}${imageUrl}` : null;

  return (
    <div style={styles.wrapper}>
      {fullImageUrl && !imgError ? (
        <img
          src={fullImageUrl}
          alt="CT 결과"
          style={styles.image}
          onError={() => setImgError(true)}
        />
      ) : (
        <div style={styles.noImage}>
          이미지를 불러올 수 없습니다.
        </div>
      )}
    </div>
  );
};

const styles = {
  wrapper: {
    display: 'flex',
    justifyContent: 'center',
    alignItems: 'center',
    marginTop: '20px',
    padding: 0,
    backgroundColor: '#fff',
    width: '100%',
  },
  image: {
    width: '100%',
    maxWidth: '800px',    // 데스크탑에서는 800px까지
    aspectRatio: '4 / 3',
    objectFit: 'contain', // 이미지 짤리지 않게
    backgroundColor: '#fff',
  }
};

export default CTImageBox;
