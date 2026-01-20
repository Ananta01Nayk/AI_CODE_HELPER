import * as vscode from "vscode";
import { execFile } from "child_process";
import * as path from "path";

export function activate(context: vscode.ExtensionContext) {

  const chatCommand = vscode.commands.registerCommand(
    "ai-code-helper.chat",
    () => {

      const panel = vscode.window.createWebviewPanel(
        "aiCodeHelperChat",
        "AI Code Helper",
        vscode.ViewColumn.One,
        { enableScripts: true }
      );

      panel.webview.html = getChatHtml();

      panel.webview.onDidReceiveMessage(async (message) => {
        if (message.type === "ask") {

          const pythonExe = path.join(
            "D:",
            "ananta",
            "AI_engineer_Intership",
            "Day3",
            "AI_CODE_HELPER",
            "helper",
            "Scripts",
            "python.exe"
          );

          const pythonScript = path.join(
            "D:",
            "ananta",
            "AI_engineer_Intership",
            "Day3",
            "AI_CODE_HELPER",
            "rag_query.py"
          );

          execFile(
            pythonExe,
            [pythonScript, message.text],
            {
              cwd: path.join(
                "D:",
                "ananta",
                "AI_engineer_Intership",
                "Day3",
                "AI_CODE_HELPER"
              )
            },
            (error, stdout, stderr) => {
              panel.webview.postMessage({
                type: "answer",
                text: error ? stderr : stdout
              });
            }
          );
        }
      });
    }
  );

  context.subscriptions.push(chatCommand);
}

function getChatHtml(): string {
  return `
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<style>
body { font-family: sans-serif; padding: 10px; }
#chat { height: 80vh; overflow-y: auto; border: 1px solid #ddd; padding: 10px; }
.user { color: blue; margin: 5px 0; }
.ai { color: green; margin: 5px 0; white-space: pre-wrap; }
#input { width: 80%; }
</style>
</head>
<body>
<h3>AI CODE HELPER</h3>
<div id="chat"></div>
<br/>
<input id="input" placeholder="Ask about your code..." />
<button onclick="send()">Send</button>

<script>
const vscode = acquireVsCodeApi();
const chat = document.getElementById("chat");

function send() {
  const input = document.getElementById("input");
  const text = input.value.trim();
  if (!text) return;

  chat.innerHTML += '<div class="user"><b>You:</b> ' + text + '</div>';
  vscode.postMessage({ type: "ask", text });
  input.value = "";
}

window.addEventListener("message", event => {
  if (event.data.type === "answer") {
    chat.innerHTML += '<div class="ai"><b>ai code helper:</b><br>' + event.data.text + '</div>';
    chat.scrollTop = chat.scrollHeight;
  }
});
</script>
</body>
</html>
`;
}

export function deactivate() {}
