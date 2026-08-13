import React, { useState } from 'react';
import './App.css';

const App = () => {
  const [sourceCode, setSourceCode] = useState('// Enter your code here...');
  const [language, setLanguage] = useState('python');
  const [target, setTarget] = useState('apk');
  const [status, setStatus] = useState('IDLE');
  const [logs, setLogs] = useState([]);

  const handleCompile = () => {
    setStatus('COMPILING');
    setLogs(['[System] Initializing Ultra-Compiler Pipeline...']);
    
    // Simulating the backend processes shown in your project
    setTimeout(() => setLogs(prev => [...prev, `[Frontend] Parsing ${language.toUpperCase()} to Universal AST...`]), 800);
    setTimeout(() => setLogs(prev => [...prev, `[IR Core] Converting AST to LLVM/Wasm Intermediate Representation...`]), 1600);
    setTimeout(() => setLogs(prev => [...prev, `[Backend] Generating binaries using native toolchains...`]), 2400);
    setTimeout(() => {
      setLogs(prev => [...prev, `[Packager] Assembling final ${target.toUpperCase()} package...`]);
      setStatus('SUCCESS');
    }, 3200);
  };

  return (
    <div className="app-container">
      <header className="app-header">
        <h1 className="gradient-text">Ultra-Compiler Studio 🚀📦🔗</h1>
        <p className="subtitle">The Universal Multi-Language Compilation & Packaging Pipeline</p>
      </header>

      <main className="dashboard">
        <section className="config-panel panel">
          <h2 className="panel-title">1. Configuration</h2>
          
          <div className="input-group">
            <label>Source Language:</label>
            <select value={language} onChange={(e) => setLanguage(e.target.value)} className="neon-select">
              <option value="python">Python (3.10+)</option>
              <option value="cpp">C / C++</option>
              <option value="java">Java / Kotlin</option>
              <option value="javascript">JavaScript</option>
            </select>
          </div>

          <div className="input-group">
            <label>Target Output:</label>
            <select value={target} onChange={(e) => setTarget(e.target.value)} className="neon-select">
              <option value="apk">Android App (.apk)</option>
              <option value="wasm">WebAssembly (WASM)</option>
              <option value="native">Native Executable</option>
            </select>
          </div>
        </section>

        <section className="editor-panel panel">
          <h2 className="panel-title">2. Source Code</h2>
          <textarea 
            className="code-editor" 
            value={sourceCode}
            onChange={(e) => setSourceCode(e.target.value)}
            spellCheck="false"
          />
          <button 
            className={`compile-btn ${status === 'COMPILING' ? 'pulsing' : ''}`}
            onClick={handleCompile}
            disabled={status === 'COMPILING'}
          >
            {status === 'COMPILING' ? 'PROCESSING PIPELINE...' : 'INITIATE BUILD'}
          </button>
        </section>

        <section className="console-panel panel">
          <h2 className="panel-title">3. Build Output</h2>
          <div className="terminal">
            {logs.length === 0 ? (
              <span className="terminal-placeholder">Awaiting compilation commands...</span>
            ) : (
              logs.map((log, index) => (
                <div key={index} className="log-line">
                  <span className="timestamp">[{new Date().toLocaleTimeString()}]</span> {log}
                </div>
              ))
            )}
            {status === 'SUCCESS' && (
              <div className="success-message">
                ✨ BUILD COMPLETE: Your {target.toUpperCase()} payload is ready.
              </div>
            )}
          </div>
        </section>
      </main>
    </div>
  );
};

export default App;
