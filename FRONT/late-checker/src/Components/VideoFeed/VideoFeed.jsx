import React from 'react';
import styled from 'styled-components'

const VideoFeed = () => {
    const VideoFeedSection = styled.section`
        display: flex;
        flex-direction: column;
        margin: 40px 10px;
        background-color: #ffffff;
        padding: 20px;
        width: 45vw;
        h2 {
            margin-top : 0;
            font-size: 45px;
            line-height: 1;
            font-weight: normal;
            color: #013087;
            text-align: center;
        }
`
    return (
            <VideoFeedSection className='some-space'>
				<h2>Video Feed</h2>
                <iframe allowFullScreen
                        title = 'camera feed'
                        webkitallowfullscreen
                        mozallowfullscreen
			// !!! TO CHANGE !!!
                        src="https://www.google.com/url?sa=i&source=images&cd=&ved=2ahUKEwik17irtsHmAhVFXSsKHQnNAu8QjRx6BAgBEAQ&url=https%3A%2F%2Fwww.facebook.com%2FRoyalCCC.jo%2Fphotos%2F&psig=AOvVaw0gXJVHoEkBWG-28d3l7bDP&ust=1576835018541497"
                        frameBorder="0"
                        width="100%"
                        height="576" />
			</VideoFeedSection>
    );
};

export default VideoFeed;
