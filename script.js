let data = [];

fetch('data.json')
  .then(res => res.json())
  .then(json => {
    data = json;
    display(data);
  })
  .catch(() => {
    document.getElementById('tableBody').innerHTML =
      "<tr><td colspan='5'>Error loading data</td></tr>";
  });

function calculateNextDue(lastInspection) {
  if (!lastInspection) return null;

  let date = new Date(lastInspection);

  // Add 6 months
  date.setMonth(date.getMonth() + 6);

  return date.toISOString().split("T")[0];
}
  function display(records) {
  const table = document.getElementById('tableBody');
  table.innerHTML = '';

  if (records.length === 0) {
    table.innerHTML = "<tr><td colspan='5'>No records found</td></tr>";
  }

  document.getElementById('count').innerText =
    "Showing " + records.length + " records";

  records.forEach(r => {
    const row = document.createElement('tr');

    let badgeClass = r.status.toLowerCase();

    row.innerHTML = `
      <td>${r.equipment_id}</td>
      <td>${r.type}</td>
      <td>${r.building}</td>
      <td>${calculateNextDue(r.last_inspection) || "N/A"}</td>
      <td><span class="badge ${badgeClass}">${r.status}</span></td>
    `;

    row.onclick = () => showDetail(r);
    table.appendChild(row);
  });
}

document.getElementById('search').addEventListener('input', filterData);
document.getElementById('filter').addEventListener('change', filterData);

function filterData() {
  const search = document.getElementById('search').value.toLowerCase();
  const filter = document.getElementById('filter').value;

  let filtered = data.filter(r =>
    r.equipment_id.toLowerCase().includes(search)
  );

  if (filter !== "ALL") {
    filtered = filtered.filter(r => r.status === filter);
  }

  display(filtered);
}

function showDetail(r) {
  const today = new Date();
  let message = "No data";

  if (r.next_due) {
    const nextDue = calculateNextDue(r.last_inspection);

if (nextDue) {
  const due = new Date(nextDue);
    const diff = Math.ceil((due - today) / (1000 * 60 * 60 * 24));

    if (diff < 0) {
      message = `❌ OVERDUE by ${Math.abs(diff)} days`;
    } else {
      message = `⚠️ ${diff} days remaining`;
    }
  }

  let prediction = "Low Confidence";
  if (r.outcome === 1) prediction = "⚠️ High Risk";
  else if (r.outcome === 0) prediction = "✅ Safe";

  document.getElementById('detail').innerHTML = `
    <div class="highlight">${message}</div>
    
    <p><b>Equipment ID:</b> ${r.equipment_id}</p>
    <p><b>Type:</b> ${r.type}</p>
    <p><b>Building:</b> ${r.building}</p>
    <p><b>Floor:</b> ${r.floor}</p>
    <p><b>Last Inspection:</b> ${r.last_inspection || "N/A"}</p>
    <p><b>Remarks:</b> ${r.remarks}</p>
    <p><b>Prediction:</b> ${prediction}</p>
  `;
}
}
