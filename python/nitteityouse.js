function trigger(){　//複数のGAS関数を、まとめて更新できるようにする関数
copySheetsBasedOnMonthAndCleanUp();
displayDatesWithKanjiWeekdays();
aggregateMentorSchedules();
matchCellColors();

}

function copySheetsBasedOnMonthAndCleanUp() {
  var spreadsheet = SpreadsheetApp.getActiveSpreadsheet();

  // 「日程調整」シートのB33からJ33の名前とB34の月を取得
  var scheduleSheet = spreadsheet.getSheetByName("日程調整");
  var names = scheduleSheet.getRange("B33:J33").getValues()[0];
  var month = scheduleSheet.getRange("B34").getValue();

  // 「メンター名」シートのデータを取得
  var mentorSheet = spreadsheet.getSheetByName("メンター名");
  var mentorData = mentorSheet.getRange("A2:B" + mentorSheet.getLastRow()).getValues();
  var mentorMap = new Map();
  mentorData.forEach(function(row) {
    mentorMap.set(row[0], row[1]); // 名前をキーとし、URLを値としてMapに格納
  });

  // すべてのシートを削除する関数
  function deleteAllSheetsExcept(exceptSheetNames) {
    var sheets = spreadsheet.getSheets();
    sheets.forEach(function(sheet) {
      if (exceptSheetNames.indexOf(sheet.getName()) === -1) {
        spreadsheet.deleteSheet(sheet);
      }
    });
  }

  // メンターの月のシートをコピーする関数
  function copyMentorMonthSheet(mentorName, month) {
    // 名前に基づいてURLを取得
    var url = mentorMap.get(mentorName);
    if (url) {
      // ファイルを開いて、対応する月のシートをコピー
      var externalSpreadsheet = SpreadsheetApp.openByUrl(url);
      var sheetName = month; // 例: "1月"
      var sheetToCopy = externalSpreadsheet.getSheetByName(sheetName);
      if (sheetToCopy) {
        var copiedSheet = sheetToCopy.copyTo(spreadsheet);
        copiedSheet.setName(mentorName); // シート名をメンターの名前に設定
      }
    }
  }

  // 「日程調整」と「メンター名」以外のシートを削除
  deleteAllSheetsExcept(["日程調整", "メンター名"]);

  // 各名前に対して、指定された月のシートをコピー
  names.forEach(function(name) {
    if (name) {
      copyMentorMonthSheet(name, month);
    }
  });
  Logger.log("copySheetsBasedOnMonthAndCleanUp");
}

function displayDatesWithKanjiWeekdays() {
  var spreadsheet = SpreadsheetApp.getActiveSpreadsheet();
  var scheduleSheet = spreadsheet.getSheetByName("日程調整");
  var selectedMonth = scheduleSheet.getRange("B34").getValue(); // 例: "1月"

  var monthNumber = parseInt(selectedMonth) - 1; // 月を数値に変換（0から始まる）
  var year = new Date().getFullYear(); // 現在の年
  var daysInMonth = new Date(year, monthNumber + 1, 0).getDate(); // その月の日数

  var weekdaysKanji = ["日", "月", "火", "水", "木", "金", "土"];
  var dates = [];
  for (var day = 1; day <= daysInMonth; day++) {
    var date = new Date(year, monthNumber, day);
    var weekday = weekdaysKanji[date.getDay()]; // 曜日を漢字に変換
    var dateString = (monthNumber + 1) + "月" + day + "日(" + weekday + ")";
    dates.push([dateString]);
  }

  // 日付を「日程調整」シートのA列に設定
  scheduleSheet.getRange(2, 1, dates.length, 1).setValues(dates);
  Logger.log("displayDatesWithKanjiWeekdays");
}

function aggregateMentorSchedules() {
  var spreadsheet = SpreadsheetApp.getActiveSpreadsheet();
  var scheduleSheet = spreadsheet.getSheetByName("日程調整");

  var selectedMonthYear = scheduleSheet.getRange("B34").getValue();
  var monthYearParts = selectedMonthYear.match(/(\d+)月/);
  var month = parseInt(monthYearParts[1]);
  var year = new Date().getFullYear();
  var daysInMonth = new Date(year, month, 0).getDate();

  var mentorNames = scheduleSheet.getRange("B33:J33").getValues()[0].filter(String);
  var times = scheduleSheet.getRange("B1:Q1").getValues()[0];
  var dates = scheduleSheet.getRange("A2:A" + (1 + daysInMonth)).getValues().flat();

  var availabilityMatrix = dates.map(() => times.map(() => []));
  var countMatrix = dates.map(() => times.map(() => 0));

  mentorNames.forEach(mentorName => {
    var mentorSheet = spreadsheet.getSheetByName(mentorName);
    if (mentorSheet) {
      var mentorAvailability = mentorSheet.getRange("B2:Q" + (1 + daysInMonth)).getValues();
      mentorAvailability.forEach((row, dateIndex) => {
        row.forEach((availability, timeIndex) => {
          if (availability === true) {
            availabilityMatrix[dateIndex][timeIndex].push(mentorName);
            countMatrix[dateIndex][timeIndex]++;
          }
        });
      });
    }
  });

  var outputMatrix = []; // 最終的な出力データを格納するための配列

  for (var i = 0; i < daysInMonth; i++) {
    var rowData = [];
    for (var j = 0; j < times.length; j++) {
      var mentorList = availabilityMatrix[i][j].join(", ");
      var count = countMatrix[i][j];
      rowData.push(count); // 出席回数
      rowData.push(mentorList); // メンターリスト
    }
    outputMatrix.push(rowData);
  }

  // バッチ処理でスプレッドシートにデータを書き込む
  scheduleSheet.getRange(2, 2, daysInMonth, times.length * 2).setValues(outputMatrix);

  Logger.log("aggregateMentorSchedules");
}

function rearrangeData(availabilityData, countData, daysInMonth) {
  var spreadsheet = SpreadsheetApp.getActiveSpreadsheet();
  var sheet = spreadsheet.getSheetByName("日程調整");

  sheet.getRange("B2:AG" + (1 + daysInMonth)).clearContent();

  availabilityData.forEach((row, rowIndex) => {
    row.forEach((cell, colIndex) => {
      var mentorList = cell.join(", ");
      var count = countData[rowIndex][colIndex];
      var newColIndex = 3 + 2 * colIndex; // C列から開始、一つ飛ばし

      sheet.getRange(rowIndex + 2, newColIndex).setValue(mentorList); // メンターリストを配置
      sheet.getRange(rowIndex + 2, newColIndex - 1).setValue(count); // 出席回数を配置
    });
  });
  Logger.log("rearrangeData");
}


function matchCellColors() {
  var spreadsheet = SpreadsheetApp.getActiveSpreadsheet();
  var sheet = spreadsheet.getSheetByName("日程調整");
  var selectedMonthYear = sheet.getRange("B34").getValue();
  var monthYearParts = selectedMonthYear.match(/(\d+)月/);
  var month = parseInt(monthYearParts[1]);
  var year = new Date().getFullYear();
  var daysInMonth = new Date(year, month, 0).getDate();

  // バッチ処理用のデータを格納する配列
  var backgrounds = [];

  // C, E, G, ...の列のセルの色をB, D, F, ...の列のセルの色に合わせる
  for (var row = 2; row <= 1 + daysInMonth; row++) {
    var rowBackgrounds = []; // 各行の背景色を格納する配列
    for (var col = 3; col <= 33; col += 2) { // C列からAG列までの奇数番目の列
      var evenColCell = sheet.getRange(row, col - 1); // 奇数番目の列の左隣（偶数番目の列）のセルの参照
      var color = evenColCell.getBackground();
      rowBackgrounds.push([color]); // バッチ処理用のデータに色を追加
    }
    backgrounds.push(rowBackgrounds); // 行ごとのデータを配列に追加
  }

  // バッチ処理でセルの背景色を一括設定
  sheet.getRange(2, 3, daysInMonth, 16).setBackgrounds(backgrounds);

  Logger.log("matchCellColors");
}

