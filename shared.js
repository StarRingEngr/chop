// ===================== 全局公共函数 =====================

// 显示短暂提示
function showToast(msg) {
  const toast = document.getElementById("toast");
  if (!toast) {
    console.warn("toast元素未找到");
    return;
  }
  toast.textContent = msg;
  toast.style.display = "block";
  setTimeout(() => toast.style.display = "none", 2000);
}

// 获取当前时间字符串（YYYY-MM-DD HH:MM:SS）
function getCurrentTime() {
  const now = new Date();
  return `${now.getFullYear()}-${String(now.getMonth()+1).padStart(2, '0')}-${String(now.getDate()).padStart(2, '0')} ${String(now.getHours()).padStart(2, '0')}:${String(now.getMinutes()).padStart(2, '0')}:${String(now.getSeconds()).padStart(2, '0')}`;
}

// 填充时间到指定输入框
function fillCurrentTime(inputId) {
  const input = document.getElementById(inputId);
  if (input) input.value = getCurrentTime();
}

// 转义HTML特殊字符（防XSS）
function escapeHtml(str) {
  if (!str) return '';
  return str.replace(/[&<>]/g, function(m) {
    if (m === '&') return '&amp;';
    if (m === '<') return '&lt;';
    if (m === '>') return '&gt;';
    return m;
  });
}

// ===================== 主题管理 =====================
let currentTheme = localStorage.getItem('theme') || 'dark';

function applyTheme(theme) {
  if (theme === 'light') {
    document.body.classList.add('light-mode');
  } else {
    document.body.classList.remove('light-mode');
  }
  currentTheme = theme;
  localStorage.setItem('theme', theme);
}

function toggleTheme() {
  const newTheme = currentTheme === 'dark' ? 'light' : 'dark';
  applyTheme(newTheme);
  const modeBtn = document.getElementById('modeToggle');
  if (modeBtn) {
    modeBtn.textContent = newTheme === 'dark' ? '切换亮色模式' : '切换暗色模式';
  }
  showToast(`已切换为${newTheme === 'dark' ? '暗色' : '亮色'}模式`);
}

function initTheme() {
  const savedTheme = localStorage.getItem('theme');
  if (savedTheme) {
    applyTheme(savedTheme);
  } else {
    applyTheme('dark');
  }
  const modeBtn = document.getElementById('modeToggle');
  if (modeBtn) {
    modeBtn.textContent = currentTheme === 'dark' ? '切换亮色模式' : '切换暗色模式';
    if (!modeBtn._listenerAttached) {
      modeBtn.addEventListener('click', toggleTheme);
      modeBtn._listenerAttached = true;
    }
  }
}

document.addEventListener('DOMContentLoaded', initTheme);