local function xml_escape(s)
  s = s:gsub("&", "&amp;")
  s = s:gsub("<", "&lt;")
  s = s:gsub(">", "&gt;")
  s = s:gsub('"', "&quot;")
  s = s:gsub("'", "&apos;")
  return s
end

local function raw_paragraph(text, keep_next, bold)
  local ppr = '<w:pPr><w:pStyle w:val="SourceCode"/>'
  if keep_next then
    ppr = ppr .. '<w:keepNext/>'
  end
  ppr = ppr .. '</w:pPr>'

  local rpr = ''
  if bold then
    rpr = '<w:rPr><w:b/></w:rPr>'
  end

  if text == "" then
    return '<w:p>' .. ppr .. '<w:r></w:r></w:p>'
  end

  return '<w:p>' .. ppr .. '<w:r>' .. rpr .. '<w:t xml:space="preserve">' .. xml_escape(text) .. '</w:t></w:r></w:p>'
end

local function prompt_table(text)
  local paragraphs = {}
  local section_headers = {
    ROLE = true,
    CONTEXT = true,
    TASK = true,
    REQUIREMENTS = true,
    ["OUTPUT FORMAT"] = true,
    ["QUALITY CHECKS"] = true,
    ["OPTIONAL CUSTOMISATION"] = true,
  }

  for line in (text .. "\n"):gmatch("(.-)\n") do
    local trimmed = line:gsub("^%s+", ""):gsub("%s+$", "")
    local keep_next = section_headers[trimmed] == true
    local bold = keep_next
    table.insert(paragraphs, raw_paragraph(line, keep_next, bold))
  end

  local body = table.concat(paragraphs)

  -- A one-cell table provides a clear copy-only boundary in Word. The prompt
  -- text is the only content in the cell, so Teacher Tip and Related prompts
  -- remain outside the copyable container.
  return '<w:tbl>'
    .. '<w:tblPr>'
    .. '<w:tblW w:w="0" w:type="auto"/>'
    .. '<w:tblBorders>'
    .. '<w:top w:val="single" w:sz="6" w:space="0" w:color="D9E1E6"/>'
    .. '<w:left w:val="single" w:sz="6" w:space="0" w:color="D9E1E6"/>'
    .. '<w:bottom w:val="single" w:sz="6" w:space="0" w:color="D9E1E6"/>'
    .. '<w:right w:val="single" w:sz="6" w:space="0" w:color="D9E1E6"/>'
    .. '<w:insideH w:val="nil"/>'
    .. '<w:insideV w:val="nil"/>'
    .. '</w:tblBorders>'
    .. '</w:tblPr>'
    .. '<w:tr><w:tc>'
    .. '<w:tcPr><w:shd w:fill="F3F6F8"/><w:tcMar>'
    .. '<w:top w:w="120" w:type="dxa"/><w:start w:w="120" w:type="dxa"/>'
    .. '<w:bottom w:w="120" w:type="dxa"/><w:end w:w="120" w:type="dxa"/>'
    .. '</w:tcMar></w:tcPr>'
    .. body
    .. '</w:tc></w:tr></w:tbl>'
end

function Para(el)
  if FORMAT:match("docx") then
    local text = pandoc.utils.stringify(el)
    if text == "Copy and paste:" then
      return pandoc.RawBlock("openxml",
        '<w:p><w:pPr><w:pStyle w:val="Label"/><w:keepNext/></w:pPr>'
        .. '<w:r><w:rPr><w:b/></w:rPr><w:t>Copy and paste:</w:t></w:r></w:p>')
    end
  end
  return nil
end

function CodeBlock(el)
  if FORMAT:match("docx") then
    return pandoc.RawBlock("openxml", prompt_table(el.text))
  end
  return nil
end

function Div(el)
  if el.classes:includes("pagebreak") then
    if FORMAT:match("docx") then
      return pandoc.RawBlock("openxml", '<w:p><w:r><w:br w:type="page"/></w:r></w:p>')
    elseif FORMAT:match("latex") or FORMAT:match("pdf") then
      return pandoc.RawBlock("latex", "\\newpage")
    end
  end
end
