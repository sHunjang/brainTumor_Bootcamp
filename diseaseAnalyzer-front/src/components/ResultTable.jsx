const ResultTable = ({
  location,
  coords,
  size,
  confidence,
  coord_x1,
  coord_y1,
  coord_x2,
  coord_y2,
  description, // ← 변경
  symptom
}) => {
  return (
    <div style={styles.wrapper}>
      <h4 style={styles.title}>세부 분석</h4>
      <table style={styles.table}>
        <tbody>
          <tr>
            <td style={styles.label0}>특징</td>
            <td style={styles.label0}>값</td>
          </tr>
          <tr>
            <td style={styles.label}>뇌 부위명</td>
            <td style={styles.value}>{location}</td>
          </tr>
          <tr>
            <td style={styles.label}>DB 좌표(x1, y1, x2, y2)</td>
            <td style={styles.value}>
              {coord_x1}, {coord_y1}, {coord_x2}, {coord_y2}
            </td>
          </tr>
          <tr>
            <td style={styles.label}>탐지 바운딩박스 좌표</td>
            <td style={styles.value}>{coords}</td>
          </tr>
          <tr>
            <td style={styles.label}>크기</td>
            <td style={styles.value}>{size}</td>
          </tr>
          <tr>
            <td style={styles.label}>신뢰도</td>
            <td style={styles.value}>{confidence}</td>
          </tr>
          <tr>
            <td style={styles.label}>주요 기능</td>
            <td style={styles.value}>{description}</td>
          </tr>
          <tr>
            <td style={styles.label}>예상 증상</td>
            <td style={styles.value}>{symptom}</td>
          </tr>
        </tbody>
      </table>
    </div>
  );
};

const styles = {
  wrapper: {
    width: '60%',
    margin: '30px auto 40px auto',
    textAlign: 'left',
  },
  title: {
    fontSize: '18px',
    marginBottom: '12px',
  },
  table: {
    width: '100%',
    borderCollapse: 'collapse',
    fontSize: '15px',
    border: '1px solid #ccc',
  },
  label0: {
    width: '30%',
    backgroundColor: '#f9f9f9',
    padding: '12px',
    borderBottom: '1px solid #ddd',
    fontWeight: 'bold',
    verticalAlign: 'top',
  },
  label: {
    width: '30%',
    padding: '12px',
    borderBottom: '1px solid #ddd',
    fontWeight: 'bold',
    verticalAlign: 'top',
  },
  value: {
    padding: '12px',
    borderBottom: '1px solid #ddd',
    backgroundColor: '#fff',
    color: '#666',
  },
};

export default ResultTable;
