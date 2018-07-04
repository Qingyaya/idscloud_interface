#include <File.au3>
#include <Array.au3>

FileChangeDir(@ScriptDir)
RunWait(@ComSpec & " /c python get_optoken.py")
Sleep(2000)
RunWait(@ComSpec & " /c python run_all_case.py")
$path=@ScriptDir & "\report"
$filelist=_FileListToArray($path)
$file=$filelist[UBound($filelist)-1]
$names=_FileListToArray($path & "\" &$file)
$name=$names[UBound($names)-1]
$reportpath = $path & "\" & $file & "\"&$name
ShellExecute($reportpath)

