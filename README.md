<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Ultra AI - Your All-in-One AI Assistant</title>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/animejs/3.2.1/anime.min.js"></script>
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;600;700&display=swap');

        :root {
            --primary-color: #6a1b9a;
            --secondary-color: #9c27b0;
            --accent-color: #e1bee7;
            --text-color: #f3e5f5;
            --background-color: #4a148c;
        }

        body {
            font-family: 'Poppins', sans-serif;
            line-height: 1.6;
            color: var(--text-color);
            background: linear-gradient(135deg, var(--background-color) 0%, var(--primary-color) 100%);
            margin: 0;
            padding: 0;
        }

        .container {
            max-width: 1200px;
            margin: 0 auto;
            padding: 2rem;
        }

        header {
            text-align: center;
            padding: 2rem 0;
            background: rgba(255, 255, 255, 0.1);
            backdrop-filter: blur(10px);
            border-radius: 20px;
            box-shadow: 0 4px 30px rgba(0, 0, 0, 0.1);
            margin-bottom: 2rem;
        }

        h1 {
            font-size: 4rem;
            margin-bottom: 0.5rem;
            color: var(--accent-color);
            text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.3);
        }

        .tagline {
            font-style: italic;
            color: var(--text-color);
        }

        nav {
            display: flex;
            justify-content: center;
            margin-top: 1rem;
        }

        nav a {
            margin: 0 1rem;
            color: var(--accent-color);
            text-decoration: none;
            font-weight: bold;
            transition: all 0.3s ease;
            position: relative;
        }

        nav a::after {
            content: '';
            position: absolute;
            width: 100%;
            height: 2px;
            bottom: -5px;
            left: 0;
            background-color: var(--accent-color);
            transform: scaleX(0);
            transition: transform 0.3s ease;
        }

        nav a:hover::after {
            transform: scaleX(1);
        }

        .features {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
            gap: 2rem;
            margin-bottom: 2rem;
        }

        .feature {
            background: rgba(255, 255, 255, 0.1);
            padding: 2rem;
            border-radius: 20px;
            box-shadow: 0 4px 30px rgba(0, 0, 0, 0.1);
            backdrop-filter: blur(5px);
            text-align: center;
            transition: transform 0.3s ease, box-shadow 0.3s ease;
            overflow: hidden;
            position: relative;
        }

        .feature::before {
            content: '';
            position: absolute;
            top: -50%;
            left: -50%;
            width: 200%;
            height: 200%;
            background: radial-gradient(circle, rgba(255,255,255,0.2) 0%, rgba(255,255,255,0) 70%);
            transform: rotate(45deg);
            transition: all 0.5s ease;
            opacity: 0;
        }

        .feature:hover::before {
            opacity: 1;
            transform: rotate(45deg) translate(50%, 50%);
        }

        .feature:hover {
            transform: translateY(-10px);
            box-shadow: 0 10px 40px rgba(0, 0, 0, 0.2);
        }

        .feature-icon {
            font-size: 3rem;
            margin-bottom: 1rem;
        }

        .demo {
            text-align: center;
            margin-bottom: 2rem;
        }

        .demo img {
            max-width: 100%;
            border-radius: 20px;
            box-shadow: 0 10px 30px rgba(0, 0, 0, 0.2);
            transition: transform 0.3s ease;
        }

        .demo img:hover {
            transform: scale(1.05);
        }

        .quickstart, .installation, .usage, .tech-stack {
            background: rgba(255, 255, 255, 0.1);
            padding: 2rem;
            border-radius: 20px;
            box-shadow: 0 4px 30px rgba(0, 0, 0, 0.1);
            backdrop-filter: blur(5px);
            margin-bottom: 2rem;
        }

        .quickstart h2, .installation h2, .usage h2, .tech-stack h2 {
            color: var(--accent-color);
            margin-bottom: 1rem;
        }

        code {
            background: rgba(0, 0, 0, 0.3);
            padding: 0.2rem 0.4rem;
            border-radius: 4px;
            font-family: monospace;
            color: var(--accent-color);
        }

        .usage-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(150px, 1fr));
            gap: 1rem;
        }

        .usage-item {
            text-align: center;
            padding: 1rem;
            background: rgba(0, 0, 0, 0.2);
            border-radius: 15px;
            transition: all 0.3s ease;
        }

        .usage-item:hover {
            background: rgba(0, 0, 0, 0.3);
            transform: translateY(-5px);
        }

        .tech-stack table {
            width: 100%;
            border-collapse: separate;
            border-spacing: 0 10px;
        }

        .tech-stack td {
            padding: 1rem;
            background: rgba(0, 0, 0, 0.2);
            border-radius: 10px;
        }

        footer {
            text-align: center;
            margin-top: 2rem;
            padding: 2rem 0;
            background: rgba(255, 255, 255, 0.1);
            backdrop-filter: blur(10px);
            border-radius: 20px;
        }

        .social-links {
            margin-top: 1rem;
        }

        .social-links a {
            display: inline-block;
            margin: 0 0.5rem;
            padding: 0.5rem 1rem;
            background: var(--secondary-color);
            color: var(--text-color);
            text-decoration: none;
            border-radius: 25px;
            transition: all 0.3s ease;
            position: relative;
            overflow: hidden;
        }

        .social-links a::before {
            content: '';
            position: absolute;
            top: 0;
            left: -100%;
            width: 100%;
            height: 100%;
            background: linear-gradient(120deg, transparent, rgba(255, 255, 255, 0.3), transparent);
            transition: all 0.5s;
        }

        .social-links a:hover::before {
            left: 100%;
        }

        .social-links a:hover {
            background: var(--primary-color);
            transform: translateY(-3px);
            box-shadow: 0 5px 15px rgba(0, 0, 0, 0.3);
        }

        @keyframes float {
            0% { transform: translateY(0px); }
            50% { transform: translateY(-20px); }
            100% { transform: translateY(0px); }
        }

        .floating {
            animation: float 6s ease-in-out infinite;
        }
    </style>
</head>
<body>
    <div class="container">
        <header>
            <h1 class="floating">Ultra AI</h1>
            <p class="tagline">Your All-in-One AI Assistant Powered by Cutting-Edge Technology</p>
            <nav>
                <a href="#features">Features</a>
                <a href="#demo">Demo</a>
                <a href="#quickstart">Quick Start</a>
                <a href="#installation">Installation</a>
                <a href="#usage">Usage</a>
                <a href="#tech-stack">Tech Stack</a>
            </nav>
        </header>

        <section id="features" class="features">
            <div class="feature">
                <div class="feature-icon">💬</div>
                <h3>AI-Powered Chat</h3>
            </div>
            <div class="feature">
                <div class="feature-icon">🎨</div>
                <h3>Image Generation</h3>
            </div>
            <div class="feature">
                <div class="feature-icon">🗣️</div>
                <h3>Voice Interaction</h3>
            </div>
            <div class="feature">
                <div class="feature-icon">✨</div>
                <h3>Prompt Engineering</h3>
            </div>
            <div class="feature">
                <div class="feature-icon">🔐</div>
                <h3>Secure Access</h3>
            </div>
            <div class="feature">
                <div class="feature-icon">🌐</div>
                <h3>Multi-Language</h3>
            </div>
            <div class="feature">
                <div class="feature-icon">📊</div>
                <h3>Analytics Dashboard</h3>
            </div>
            <div class="feature">
                <div class="feature-icon">🔄</div>
                <h3>Model Switching</h3>
            </div>
            <div class="feature">
                <div class="feature-icon">📱</div>
                <h3>Responsive Design</h3>
            </div>
            <div class="feature">
                <div class="feature-icon">🧠</div>
                <h3>Continuous Learning</h3>
            </div>
        </section>

        <section id="demo" class="demo">
            <h2>Demo</h2>
            <p>Check out Ultra AI in action:</p>
            <img src="https://img.youtube.com/vi/-YeUZHr1w6E/0.jpg" alt="Ultra AI Demo">
        </section>

        <section id="quickstart" class="quickstart">
            <h2>Quick Start</h2>
            <code>git clone https://github.com/GanapathySubramaniam/God-s-eye.git</code><br>
            <code>cd ultra-ai</code><br>
            <code>pip install -r requirements.txt</code><br>
            <code>streamlit run Login.py</code>
        </section>

        <section id="installation" class="installation">
            <h2>Installation</h2>
            <details>
                <summary><strong>Click to expand detailed installation steps</strong></summary>
                <ol>
                    <li><strong>Clone the repository</strong><br>
                    <code>git clone https://github.com/GanapathySubramaniam/God-s-eye.git</code><br>
                    <code>cd ultra-ai</code></li>
                    <li><strong>Set up virtual environment (optional but recommended)</strong><br>
                    <code>python -m venv venv</code><br>
                    <code>source venv/bin/activate  # On Windows use `venv\Scripts\activate`</code></li>
                    <li><strong>Install dependencies</strong><br>
                    <code>pip install -r requirements.txt</code></li>
                    <li><strong>Configuration</strong><br>
                    Create <code>.env</code> in <code>models/</code> directory:<br>
                    <code>OPENAI=your_openai_api_key_here</code><br>
                    <code>ANTHROPIC=your_anthropic_api_key_here</code><br>
                    Set password in <code>pwd.txt</code>:<br>
                    <code>your_chosen_password_here</code><br>
                    <em>⚠️ Use a strong, unique password. Never share or commit this file.</em></li>
                    <li><strong>Run the application</strong><br>
                    <code>streamlit run Login.py</code></li>
                </ol>
            </details>
        </section>

        <section id="usage" class="usage">
            <h2>Usage</h2>
            <div class="usage-grid">
                <div class="usage-item">
                    <div class="feature-icon">🔑</div>
                    <strong>Login</strong>
                </div>
                <div class="usage-item">
                    <div class="feature-icon">💬</div>
                    <strong>Chat</strong>
                </div>
                <div class="usage-item">
                    <div class="feature-icon">🖼️</div>
                    <strong>Generate Images</strong>
                </div>
                <div class="usage-item">
                    <div class="feature-icon">🎤</div>
                    <strong>Voice Interact</strong>
                </div>
                <div class="usage-item">
                    <div class="feature-icon">✍️</div>
                    <strong>Craft Prompts</strong>
                </div>
            </div>
        </section>

        <section id="tech-stack" class="tech-stack">
            <h2>Tech Stack</h2>
            <table>
                <tr>
                    <td><strong>Frontend</strong></td>
                    <td><strong>AI Models</strong></td>
                    <td><strong>Backend</strong></td>
                    <td><strong>Other</strong></td>
                </tr>
                <tr>
                    <td>Streamlit</td>
                    <td>Claude (Anthropic)<br>GPT-3.5 (OpenAI)<br>DALL-E 3 (OpenAI)<br>Whisper (OpenAI)</td>
                    <td>Python 3.7+</td>
                    <td>Custom Auth<br>Git</td>
                </tr>
            </table>
        </section>

        <footer>
            <h3>Connect with the Creator</h3>
            <div class="social-links">
                <a href="https://ganapathysubramaniam.github.io/" target="_blank">Portfolio</a><a href="https://github.com/GanapathySubramaniam" target="_blank">GitHub</a>
            </div>
            <p>Built with ❤️ by Ganapathy Subramaniam Sundar</p>
        </footer>
    </div>

    <script>
        // Animate features on scroll
        const features = document.querySelectorAll('.feature');
        features.forEach((feature, index) => {
            anime({
                targets: feature,
                opacity: [0, 1],
                translateY: [50, 0],
                delay: index * 100,
                duration: 1000,
                easing: 'easeOutQuad',
                autoplay: false
            });
        });

        // Intersection Observer to trigger animations
        const observer = new IntersectionObserver((entries) => {
            entries.forEach(entry => {
                if (entry.isIntersecting) {
                    anime({
                        targets: entry.target,
                        opacity: [0, 1],
                        translateY: [50, 0],
                        duration: 1000,
                        easing: 'easeOutQuad'
                    });
                    observer.unobserve(entry.target);
                }
            });
        }, { threshold: 0.1 });

        document.querySelectorAll('section').forEach(section => {
            observer.observe(section);
        });

        // Smooth scroll for navigation
        document.querySelectorAll('nav a').forEach(anchor => {
            anchor.addEventListener('click', function (e) {
                e.preventDefault();
                document.querySelector(this.getAttribute('href')).scrollIntoView({
                    behavior: 'smooth'
                });
            });
        });

        // Parallax effect for header
        window.addEventListener('scroll', () => {
            const scrollPosition = window.pageYOffset;
            document.querySelector('header').style.backgroundPositionY = scrollPosition * 0.5 + 'px';
        });

        // Typing effect for tagline
        const tagline = document.querySelector('.tagline');
        const text = tagline.textContent;
        tagline.textContent = '';
        let i = 0;
        function typeWriter() {
            if (i < text.length) {
                tagline.textContent += text.charAt(i);
                i++;
                setTimeout(typeWriter, 50);
            }
        }
        typeWriter();

        // Interactive feature cards
        features.forEach(feature => {
            feature.addEventListener('mousemove', (e) => {
                const rect = feature.getBoundingClientRect();
                const x = e.clientX - rect.left;
                const y = e.clientY - rect.top;
                feature.style.setProperty('--mouse-x', `${x}px`);
                feature.style.setProperty('--mouse-y', `${y}px`);
            });
        });

        // Animated background
        const canvas = document.createElement('canvas');
        const ctx = canvas.getContext('2d');
        document.body.appendChild(canvas);

        canvas.width = window.innerWidth;
        canvas.height = window.innerHeight;

        const particles = [];

        class Particle {
            constructor() {
                this.x = Math.random() * canvas.width;
                this.y = Math.random() * canvas.height;
                this.size = Math.random() * 5 + 1;
                this.speedX = Math.random() * 3 - 1.5;
                this.speedY = Math.random() * 3 - 1.5;
            }
            update() {
                this.x += this.speedX;
                this.y += this.speedY;
                if (this.size > 0.2) this.size -= 0.1;
            }
            draw() {
                ctx.fillStyle = 'rgba(225, 190, 231, 0.8)';
                ctx.beginPath();
                ctx.arc(this.x, this.y, this.size, 0, Math.PI * 2);
                ctx.fill();
            }
        }

        function handleParticles() {
            for (let i = 0; i < particles.length; i++) {
                particles[i].update();
                particles[i].draw();
                if (particles[i].size <= 0.2) {
                    particles.splice(i, 1);
                    i--;
                }
            }
        }

        function createParticles() {
            if (particles.length < 100) {
                particles.push(new Particle());
            }
            requestAnimationFrame(createParticles);
        }

        function animate() {
            ctx.clearRect(0, 0, canvas.width, canvas.height);
            handleParticles();
            requestAnimationFrame(animate);
        }

        createParticles();
        animate();

        // Resize canvas on window resize
        window.addEventListener('resize', () => {
            canvas.width = window.innerWidth;
            canvas.height = window.innerHeight;
        });
    </script>
</body>
</html>
