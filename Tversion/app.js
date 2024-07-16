// Set up the scene, camera, and renderer
const scene = new THREE.Scene();
const camera = new THREE.PerspectiveCamera(75, window.innerWidth / window.innerHeight, 0.1, 1000);
const renderer = new THREE.WebGLRenderer();
renderer.setSize(window.innerWidth, window.innerHeight);
document.body.appendChild(renderer.domElement);

// Create a geometry for the space-time diagram
const geometry = new THREE.BufferGeometry();
const vertices = [];

// Define the parameters for the space-time diagram
const tMin = -10, tMax = 10;
const xMin = -10, xMax = 10;
const yMin = -10, yMax = 10;
const dt = 0.1, dx = 0.1, dy = 0.1;

// Create the grid for the space-time diagram
for (let t = tMin; t <= tMax; t += dt) {
    for (let x = xMin; x <= xMax; x += dx) {
        for (let y = yMin; y <= yMax; y += dy) {
            vertices.push(x, y, 0); // Z is set to zero for a 3D space-time diagram
        }
    }
}

geometry.setAttribute('position', new THREE.Float32BufferAttribute(vertices, 3));

// Create a material and mesh for the space-time diagram
const material = new THREE.PointsMaterial({ color: 0xffffff, size: 0.1 });
const points = new THREE.Points(geometry, material);
scene.add(points);

// Set the camera position
camera.position.z = 50;

// Add a slider control for time
const timeSlider = document.getElementById('timeSlider');
const timeLabel = document.getElementById('timeLabel');

timeSlider.addEventListener('input', (event) => {
    const timeValue = event.target.value;
    timeLabel.textContent = timeValue;
    updateVisualization(timeValue);
});

function updateVisualization(timeValue) {
    // Update the visualization based on the new time value
    // For example, update the position of the points in the space-time diagram
    // ...
}

// Animation loop
function animate() {
    requestAnimationFrame(animate);
    renderer.render(scene, camera);
}

animate();