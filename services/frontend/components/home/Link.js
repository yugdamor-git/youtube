import React, { useState, useEffect } from "react";
import Loading from "../ui/Loading";
import Video from "./Video";


async function fetchThumbnailData(url) {

  const response = await fetch(`http://148.251.41.232:1337/download/thumbnail?url=${url}`);

  const data = await response.json();

  console.log(data)

  return data;
}


async function fetchData(url) {

  const response = await fetch(`http://148.251.41.232:1337/info?url=${url}`);

  const data = await response.json();

  console.log(data)

  return data;
}

function scrollDown(downloadType) {
  let elem = null;
  if (downloadType == "thumbnail") {
    elem = document.getElementById("thumbnailDownload");
  } else {
    elem = document.getElementById("downloadSection");
  }
  if (elem != null) {
    if (downloadType == "thumbnail") {
      elem.scrollIntoView({
        behavior: "smooth",
        block: "start",
        inline: "nearest",
      });
    } else {
      elem.scrollIntoView({
        behavior: "smooth",
        block: "center",
        inline: "nearest",
      });
    }
  }
}

const Link = ({ data,contentType }) => {
  const [isUrl, setIsUrl] = useState("");
  const [inputVal, setInputVal] = useState("");
  const [loading, setLoading] = useState(false);
  const [showVid, setShowVid] = useState(false);

  const [currentVideoData,setCurrentVideoData] = useState(null)



  ///////////// validate url function //////////
  const validURL = async(str) => {
    // var pattern = new RegExp(
    //   "^(https?:\\/\\/)?" + // protocol
    //     "((([a-z\\d]([a-z\\d-]*[a-z\\d])*)\\.)+[a-z]{2,}|" + // domain name
    //     "((\\d{1,3}\\.){3}\\d{1,3}))" + // OR ip (v4) address
    //     "(\\:\\d+)?(\\/[-a-z\\d%_.~+]*)*" + // port and path
    //     "(\\?[;&a-z\\d%_.~+=-]*)?" + // query string
    //     "(\\#[-a-z\\d_]*)?$",
    //   "i"
    // ); // fragment locator
    var pattern = new RegExp(
      "^(https?\:\/\/)?(www\.youtube\.com|youtu\.be|youtube\.com)\/.+$",
      "i"
    ); // fragment locator
    setIsUrl(pattern.test(str));

    if (pattern.test(str)) {
      setLoading(true);
      /// fetch function here
      let data = null
      if (contentType == "video" || contentType == "audio")
      {
         data = await fetchData(str)
      }
      else
      {
        data = await fetchThumbnailData(str)
      }
      

      setCurrentVideoData(data.data)
        setLoading(false);
        setShowVid(true);

        setTimeout(()=>{
          scrollDown("video")
        },300)

    }

    return !!pattern.test(str);
  };

  useEffect(() => {
    if (inputVal.length == 0) {
      setIsUrl("");
    } else {
      validURL(inputVal);
    }
  }, [inputVal]);

  ////////// get video function ////////
  const getVideoHandler = async(e) => {
    e.preventDefault();
    if (isUrl) {
      setLoading(true);
      /// fetch function here
      console.log("started")

     const data = await fetchData(isUrl)

      setCurrentVideoData(data)
      
      console.log(data)
      
      setLoading(false);
      setShowVid(true);
    }
  };
  return (
    <div className="text-center mt-12 mb-11 text-[#343a40] ">
      <h1 className="font-medium sm:text-[40px] text-2xl w-[20rem] sm:w-full sm:mb-2 m-auto">
        {data.title}
      </h1>
      <p className=" mb-4 mx-[15px]">{data.p}</p>

        <div
          className="custom:w-5/6 w-[350px] sm:w-[650px] lg:w-[778px] sm:my-[28px]  mx-auto sm:flex sm:justify-center md-w[960px]"
        >
          <div className="mb-2 sm:w-[450px] md:w-[640px] lg:w-[760px]   ">
            <input
              type="search"
              className="sm:w-[495px] lg:w-[630px] outline-none py-[14px] px-5  text-[#4b4c4d] text-[14px] rounded-xl block w-full border-2 border-[#ffc4c4]"
              placeholder={data.placeholder}
              value={inputVal}
              onChange={(e) => {
                setInputVal(e.target.value);
              }}
              required
            />
          </div>

          <button
            type="submit"
            onClick={()=>validURL(inputVal)}
            className=" text-white w-[100%] h-[50px] sm:w-[152px] sm:h-[52px] font-[600] bg-[#fd0054] hover:bg-[#dc2260] focus:outline-none  rounded-lg  text-center text-[17px] shadow-2xl"
          >
            {data.button}
          </button>
        </div>

      {isUrl && loading && <Loading />}
      {showVid && <Video contentType={contentType} currentVideoData={currentVideoData} />}
      {inputVal.length > 0 && !isUrl && (
        <p className="text-[#dc3545] text-center mt-1">{data.wrong}</p>
      )}

     
    </div>
  );
};

export default Link;
